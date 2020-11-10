#ifndef DMOMINTADDRESSVALIDATOR_H
#define DMOMINTADDRESSVALIDATOR_H

#include <QValidator>

/** Base58 entry widget validator.
   Corrects near-miss characters and refuses characters that are not part of base58.
 */
class DMOmintAddressValidator : public QValidator
{
    Q_OBJECT

public:
    explicit DMOmintAddressValidator(QObject *parent = 0);

    State validate(QString &input, int &pos) const;

    static const int MaxAddressLength = 49;
};

#endif // DMOMINTADDRESSVALIDATOR_H
